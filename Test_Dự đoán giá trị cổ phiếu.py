import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Đọc từng file CSV và thêm cột 'Ticker' để phân biệt các mã cổ phiếu
df_fpt = pd.read_csv(r'C:/Users/phung/Downloads/FPT.csv')
df_fpt['Ticker'] = 'FPT'

df_mns = pd.read_csv(r'C:/Users/phung/Downloads/MSN.csv')
df_mns['Ticker'] = 'MSN'

df_pnj = pd.read_csv(r'C:/Users/phung/Downloads/PNJ.csv')
df_pnj['Ticker'] = 'PNJ'

df_vic = pd.read_csv(r'C:/Users/phung/Downloads/VIC.csv')
df_vic['Ticker'] = 'VIC'

# Hợp nhất các DataFrame lại thành một
df = pd.concat([df_fpt, df_mns, df_pnj, df_vic], ignore_index=True)

# Tính toán biến động giá cổ phiếu: Giá tại thời điểm t+1 - Giá hiện tại
df['price_change'] = df['Close'].shift(-1) - df['Close']

# Loại bỏ các hàng có giá trị NaN(Not a Number) (do shift tạo ra)
df = df.dropna()

# Hàm dự đoán và đánh giá cho từng mã cổ phiếu
def train_and_evaluate_by_ticker(df, ticker):
    print(f"--- Dự đoán cho mã cổ phiếu: {ticker} ---")
    
    # Lọc dữ liệu theo mã cổ phiếu
    df_ticker = df[df['Ticker'] == ticker]
    
    # Biến độc lập (giá hiện tại, khối lượng)
    X = df_ticker[['Close', 'Volume']]
    
    # Biến phụ thuộc (biến động giá)
    y = df_ticker['price_change']
    
    # Chia dữ liệu thành tập huấn luyện và tập kiểm thử
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Chuẩn hóa dữ liệu
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Khởi tạo mô hình
    model = LinearRegression()
    
    # Huấn luyện mô hình
    model.fit(X_train_scaled, y_train)
    
    # Dự đoán trên tập kiểm thử
    y_pred = model.predict(X_test_scaled)
    
    # Đánh giá mô hình
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Squared Error(chỉ số đo độ chính xác của mô hình): {mse}")
    print(f"R-squared(tỷ lệ phần trăm của sự biến động): {r2}")
    
    # Vẽ biểu đồ so sánh kết quả thực tế và dự đoán
    plt.figure(figsize=(12,8))
    plt.plot(y_test.values, label='Actual Price Change(Thay đổi giá thực tế)', color='blue')
    plt.plot(y_pred, label='Predicted Price Change(Dự đoán thay đổi giá)', color='red')
    plt.title(f'Actual vs Predicted Price Change for(Thay đổi giá thực tế so với dự đoán cho) {ticker}')
    plt.legend()
    plt.show()

# Gọi hàm cho từng mã cổ phiếu
tickers = df['Ticker'].unique()
for ticker in tickers:
    train_and_evaluate_by_ticker(df, ticker)
    
