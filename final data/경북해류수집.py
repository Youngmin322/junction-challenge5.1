"""
경북(경상북도) 관측소의 실시간 유향/유속 데이터를 수집해 CSV로 저장한다.

대상 API 2종 (해류도 오픈API 활용 가이드.md 참고):
- 해양관측부이 최신 관측데이터 (twRecent) : 지점 실측, obsCode 단위 1건
- 해수유동 관측소 실측 유향·유속 (hfCurrent, HF-RADAR) : 격자 실측, obsCode 단위 다건

경북 관측소 판단 근거:
- TW_0095 고래불해수욕장 -> 경북 영덕군
- KG_0101 / KG_0102 울릉도북동·북서 -> 경북 울릉군
- HF_0071 포항항 -> 경북 포항시
- HF_0073 동해남부는 정확한 관할 해역이 hwp 원문에 명시되지 않아 경북 인근으로 추정만 하고 기본 제외함.
  포함하려면 HF_STATIONS에 추가할 것.
"""

import csv
import sys
from pathlib import Path

import requests

SERVICE_KEY = "hPO24vIqtkE4lTbc6jwu62RSfYswym8X0ioMC3VgMJWFAlbtJZLIJmHCqyU2nbDPbkERu3T7RYleJWeqzbudgQ=="

TW_ENDPOINT = "https://apis.data.go.kr/1192136/twRecent/GetTWRecentApiService"
HF_ENDPOINT = "https://apis.data.go.kr/1192136/hfCurrent/GetHFCurrentApiService"

TW_STATIONS = {
    "TW_0095": "고래불해수욕장(영덕)",
    "KG_0101": "울릉도북동",
    "KG_0102": "울릉도북서",
}

HF_STATIONS = {
    "HF_0071": "포항항",
}

CSV_COLUMNS = [
    "api", "obsCode", "station_alias", "obsvtrNm", "lot", "lat",
    "obsrvnDt", "crdir", "crsp", "wndrct", "wspd", "wtem", "slnty",
]


def fetch_tw(obs_code: str, num_of_rows: int = 20) -> list[dict]:
    params = {
        "serviceKey": SERVICE_KEY,
        "type": "json",
        "obsCode": obs_code,
        "numOfRows": num_of_rows,
        "pageNo": 1,
    }
    resp = requests.get(TW_ENDPOINT, params=params, timeout=15)
    resp.raise_for_status()
    return _extract_items(resp.json(), api="twRecent", obs_code=obs_code)


def fetch_hf(obs_code: str, num_of_rows: int = 300) -> list[dict]:
    params = {
        "serviceKey": SERVICE_KEY,
        "type": "json",
        "obsCode": obs_code,
        "numOfRows": num_of_rows,
        "pageNo": 1,
    }
    resp = requests.get(HF_ENDPOINT, params=params, timeout=15)
    resp.raise_for_status()
    return _extract_items(resp.json(), api="hfCurrent", obs_code=obs_code)


def _extract_items(payload: dict, api: str, obs_code: str) -> list[dict]:
    header = payload.get("header", {})
    if header.get("resultCode") != "00":
        print(f"[경고] {api} {obs_code}: {header.get('resultMsg')}", file=sys.stderr)
        return []

    item = payload.get("body", {}).get("items", {}).get("item", [])
    if isinstance(item, dict):
        item = [item]

    for row in item:
        row["api"] = api
        row["obsCode"] = obs_code
    return item


def main():
    out_path = Path(__file__).parent / "경북_유향유속_관측데이터.csv"
    rows = []

    for obs_code, alias in TW_STATIONS.items():
        print(f"조회 중: twRecent {obs_code} ({alias})")
        for row in fetch_tw(obs_code):
            row["station_alias"] = alias
            rows.append(row)

    for obs_code, alias in HF_STATIONS.items():
        print(f"조회 중: hfCurrent {obs_code} ({alias})")
        for row in fetch_hf(obs_code):
            row["station_alias"] = alias
            rows.append(row)

    with out_path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"완료: {len(rows)}건 저장 -> {out_path}")


if __name__ == "__main__":
    main()
