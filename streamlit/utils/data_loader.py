"""
=========================================================================
Project:
- Customer Relationship Management

Module:
- utils

File:
- data_loader.py

Purpose:
- Streamlit 화면에서 사용하는 샘플 데이터 생성 기능을 제공합니다.

Author: @nobrain711
Created: 2026-03-13

Updated:
- 2026-03-13: initial version (@nobrain711)
=========================================================================
"""

from pandas import DataFrame
from typing import Dict, List

def get_leaderboard_data() -> DataFrame:
    """
    모델 리더보드 데이터를 반환합니다.
    """
    leaderboard_data = DataFrame(
        {
            "모델명(Model)": [
                "HistGradientBoosting",
                "XGBoost",
                "EasyEnsemble",
                "Random Forest",
                "Logistic Regression",
                "LightGBM",
            ],
            "정확도(Acc)": [0.9858, 0.9729, 0.7698, 0.8375, 0.8761, 0.9000],
            "재현율(Recall)": [0.9369, 0.9800, 0.9800, 0.7389, 0.9588, 0.8900],
            "ROC-AUC": [0.9979, 0.9720, 0.9701, 0.9476, 0.8926, 0.9469],
            "PR-AUC": [0.9901, 0.9600, 0.8868, 0.9246, 0.9764, 0.9523],
            "F1-score": [0.9556, 0.9800, 0.5800, 0.7877, 0.9286, 0.9231],
        }
    ).sort_values(by="ROC-AUC", ascending=False)

    return leaderboard_data


def get_impact_data() -> DataFrame:
    """
    SHAP 예시용 feature 영향력 데이터를 반환합니다.
    """
    impact_df = DataFrame(
        {
            "feature": [
                "총 결제 금액",
                "소득 구간",
                "총 결제 횟수",
                "한도 소진율",
                "리볼빙 잔액",
            ],
            "영향력": [0.55, 0.45, 0.38, 0.25, 0.18],
        }
    ).sort_values(by="영향력")

    return impact_df


def get_model_guides() -> Dict[str, List[str]]:
    """
    모델별 전략 가이드 데이터를 반환합니다.
    """
    return {
        "HistGradientBoosting": [
            "대용량 데이터 미세 패턴 포착",
            "과적합 위험(Noise)",
            "Random Forest 교차 타겟팅",
        ],
        "XGBoost": [
            "정확도/재현율 밸런스 에이스",
            "복잡한 비선형 해석 난해",
            "Logistic Regression 보조 활용",
        ],
        "EasyEnsemble": [
            "이탈자 전수 탐지(Recall 0.98)",
            "마케팅 비용 낭비 우려",
            "LightGBM 기반 예산 효율화",
        ],
        "Random Forest": [
            "안정적인 일반화 성능",
            "정교한 신호 탐지 한계",
            "HistGBM 모델 고도화 추천",
        ],
        "LightGBM": [
            "실시간 오퍼 최적화 속도",
            "소량 데이터 취약성",
            "XGBoost와 상호 보완",
        ],
        "Logistic Regression": [
            "명확한 원인 설명력",
            "비선형 관계 포착 한계",
            "앙상블 모델 병행 사용",
        ],
    }