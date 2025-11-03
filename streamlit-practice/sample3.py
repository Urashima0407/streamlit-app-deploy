import streamlit as st

st.title("サンプルアプリ③: データ表示アプリ")

# サイドバーの作成
st.sidebar.header("設定")
option = st.sidebar.selectbox(
    "表示するデータを選択してください:",
    ("データ1", "データ2", "データ3")
)

# メインコンテンツ
st.header(f"選択されたデータ: {option}")

if option == "データ1":
    st.write("**データ1の詳細:**")
    st.write("- 項目A: 100")
    st.write("- 項目B: 200")
    st.write("- 項目C: 300")
    
    # 簡単なチャート
    import pandas as pd
    data = pd.DataFrame({
        '項目': ['A', 'B', 'C'],
        '値': [100, 200, 300]
    })
    st.bar_chart(data.set_index('項目'))

elif option == "データ2":
    st.write("**データ2の詳細:**")
    st.write("- 項目X: 150")
    st.write("- 項目Y: 250")
    st.write("- 項目Z: 350")
    
    # 簡単なチャート
    import pandas as pd
    data = pd.DataFrame({
        '項目': ['X', 'Y', 'Z'],
        '値': [150, 250, 350]
    })
    st.line_chart(data.set_index('項目'))

else:  # データ3
    st.write("**データ3の詳細:**")
    st.write("- 項目P: 120")
    st.write("- 項目Q: 220")
    st.write("- 項目R: 320")
    
    # 簡単なチャート
    import pandas as pd
    data = pd.DataFrame({
        '項目': ['P', 'Q', 'R'],
        '値': [120, 220, 320]
    })
    st.area_chart(data.set_index('項目'))

# フッター
st.markdown("---")
st.write("💡 サイドバーから異なるデータを選択してグラフの変化を確認してください！")
