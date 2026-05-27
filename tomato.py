import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# -----------------------------
# 예시 모델 (실제로는 학습된 모델 사용)
# -----------------------------
# 더미 학습 데이터
X_train = pd.DataFrame({
    "내부온도": [10, 15, 20, 25, 30]
})

y_train = [95.2, 91.5, 87.9, 84.3, 80.1]

# 모델 학습
rf_model = RandomForestRegressor()
rf_model.fit(X_train, y_train)

# -----------------------------
# 화면 구성
# -----------------------------
st.title("📊 외부 데이터 예측")

st.subheader("[ 외부 데이터 예측 ]")

# 사용자 입력
temp = st.number_input("내부온도 입력", value=20)

# 예측 버튼
if st.button("예측 실행"):

    # DataFrame 변환
    input_data = pd.DataFrame([[temp]], columns=["내부온도"])

    # 예측
    predicted = rf_model.predict(input_data)

    # 결과 출력
    st.success(f"예측 착과율 : {predicted[0]:.1f}%")