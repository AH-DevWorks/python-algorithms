# python-algorithms

## 簡介
   + 這個倉庫（Repository）包含我在學習和實踐 Python 過程中的參考課程、資源、建立的各種基礎小型演算法專案以及成果等。
   + 這些專案都是基於線上課程中的教學內容進一步延伸、擴充而成，每個專案都展示了部份的 Python 概念和技術，反映我個人的學習和技能成長歷程。

## 課程參考
+ Udemy - [100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)
  + 課程涵蓋了 Python 從基礎語法、流程控制及演算法、網頁開發，到資料科學、AI等進階主題知識。
+ Udemy - [以 SQLite 入門 SQL | Introduction to SQL with SQLite](https://www.udemy.com/course/introduction-to-sql-with-sqlite)
  + 課程從 SQL 基本觀念、實作到測驗循序漸進，內容涵蓋建立學習環境、資料表選擇、運算符與函數的應用、排序、篩選、條件邏輯、分組與聚合、子查詢以及資料表關聯，學習在自己的電腦上建立 SQLite 環境，並掌握關聯式資料庫與 SQL 查詢語法等基礎技能。
+ Udemy - [机器学习 A-Z (Machine Learning A-Z in Chinese)](https://www.udemy.com/course/machinelearningchinese/)
  + 學習機器學習的完整知識體系，從資料前處理、回歸、分類、聚類、關聯規則，到強化學習、自然語言處理、深度學習、降維與模型選擇等各個面向；透過 Python 和 R 的程式碼範本及案例，掌握構建並運用機器學習模型的能力
+ 線上資源 - [《Hello 演算法》](https://www.hello-algo.com/zh-hant/)

## 專案列表
+ 依完成日期排序（遞減）
> 執行方式： 1. 下載或 clone 此倉庫； 2. 進入對應的資料夾，如：`cd "子資料夾名稱"`； 3. 在該資料夾中使用命令提示字元 (CMD) 或終端機執行 Python 檔案，如： `python (檔名).py`。
>> 另可參考各專案資料夾內執行截圖檔案。

1. [SplitBill](./SplitBill/)
  + **帳單分攤計算器**
    + 協助計算並分攤帳單（包含小費比例10% / 12% /15%）
    + 防呆設計，避免無效或複數輸入（如輸入非數字、輸入負值或輸入超出指定範圍外的小費比例）
  + **使用的主要技術/概念**
    + 以while loop搭配conditions進行防呆設計，避免使用者輸入非數字(如英文字母)、負值或是超出指定範圍(10/12/15%)的小費數值
    + 搭配錯誤提示文字，讓使用者重新輸入直到合理為止
  + 完成日期: *[2025-02-25]*
  + <span style="color: darkorange">未來預計延伸/改進：</span>
    + 目前小費只能固定選擇 `10 / 12 / 15`，可拓展讓使用者自訂小費比例
    + 目前程式是按照總金額 / 總人數平均分攤帳單，可增加功能讓使用者各付各的帳
    + 把程式變成網頁版 WEB 應用程式
    + 儲存金額計算的歷史紀錄

2. [Theme Park Ticketing](./Theme%20Park%20Ticketing)
  + **遊樂園門票計算器**
    + 身高限制（120cm以上才可入園）
    + 依照年齡區分不同票價：11歲以下兒童$5｜12～18歲$7｜19歲以上$12
    + 拍紀念照額外加$3
    + 年齡45~55歲有特別優惠，完全免費
  + **使用的主要技術/概念**
    + 以while loop搭配conditions防呆
    + 以巢狀if-elif-else判斷是否可入園、依年齡計算票價、依拍紀念照與否來計算加價等
    + 以.lower()函式判斷使用者「是否加購紀念照」之輸入（"y"/"n"）以避免英文大小寫誤判
    + print輸出最後應支付之總金額
  + 完成日期: *[2025-02-25]*
  + <span style="color: darkorange">未來預計延伸/改進：</span>
    + 強化身高 / 年齡驗證（限定範圍，避免不合理數值）

3. [待持續更新]




*首次建立：[2025-02-25]*  
*最後更新: [2025-02-25]*