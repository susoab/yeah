## Hello guys
 - Im looking foward to meeting with you~ 
#### What's this & for what? 
 - This's a memo like a for output & memory

#### My introduce
 - i'm *** 
 - usually I went to anywhere but alone huh
 - if you dont understand japanese style, you don't care about me
 - be hunble shit down
 - I usually live in HCMC. But I was born in JP
 - anytime I can do for anybody 
-----
### Memo(It's a snippet like how to every tech tool)
#### How to use git?(like a snippet)
 - change to branch
   - git checkout
 - 前回コミット(HEAD)からの差分
   - git diff HEAD
 - ステージングエリアとHEADとの差分
   - git diff --staged
   - git diff --cached
 - 自分がしたコミットを確認
   - git log -p --name-only (修正したファイル一覧)
   - git log -p (変更内容差分, ファイル名を引数で渡すと単体で指定可)
   - git log -p --ignore-space-change (スペースや改行で差分が見づらいとき)
 - masterブランチを最新に更新(masterブランチなう)
   - git  pull --rebase origin master
 - 修正したソースコードを再度コミットしてプッシュ
   - git add ***
   - git commit -m "***"
   - git push origin add-***
 - check into log
   - git log
   - git --no-pager log
 - 修正したファイルをすべてaddしたいなら、-u が便利
   - git add -u
 - コミット詳細
   - git show 
 - delate to file
   - git rm ***
 - masterの内容を開発ブランチに反映
   - git pull origin master
 - branchを作る上と同時にそこへcheckout
   - git checkout -b [branch name] origin/master
 - branch snippet
   - git checkout -b [branch name] origin/master
   - git branch -a（for check)
     - まだmasterに何もない場合は何か作成
     - 既にmasterに何かあってpullしたい(git pull origin master)
   - git add *** 
   - git commit
   - git push origin [branch name]
   - git branch -a（for check)
   - git checkout master
   - git merge test
   - git push
 - これ分からん
   - git checkout -b *** origin/master
 - githubであらかじめリポジトリを作っておいて、そこをpush先に指定。
   - git remote add origin [url of リポジトリ] 
 - git commit → vim
   - u : like a cntl+z
   - :wq : finish(easy)
 - sample words for commit -m
   - https://anond.hatelabo.jp/20160725092419
   - Add ~
   - Fix ~
   - Update	~
   - Remove ~
   - Use ~
   - Don't ~
   - Make	~
   - Move ~
   - Change ~
   - Rename ~
   - Improve ~
   - Avoid ~
   - Allow ~
   - Implement ~
   - Handle	~

##### How to use anaconda?
 - Distribution of python
 - Into jupyter or spyder or something

##### How to use jupyter?
 - run call: control + enter
 - command: jupyter notebook + enter
 - how to up graph?: write markdown
 - finish: control + c
 - tt

##### How to use spyder?
 - for python

##### How to Oauth<br>
 - リクエストトークンを発行
 - リクエストトークンを使ってアプリ認証画面に飛ばす
 - コールバックURLでアクセストークンを取得
 - アクセストークンを使ってAPIを呼ぶ


##### En snippet(like a buzz words)
 - jesus crist
 - kinda wanna gonna gatta
 - whatever whenever however 
 - how's going on 
 - 

##### how to get AWS record(maybe until afret a year)
 - learn(should buy some book or ass dig)
 - I have to get this one cuz wanna get more ass skill

##### GraphQLについて
 - GraphQLはAPIへの問い合わせ言語(apiのインターフェース)
 - クライアントとサーバー間のデータのやり取りを容易に記述するためのクエリ言語
 - GraphQLはFacebookにより開発されたオープンソースの言語です。API作成の仕組みとしてRESTの代わりに使える
 - GraphQLの定義に従ってクエリを書き, サーバーと通信を取ることでJSONになって戻る
 - APIといえばRESTfulなendpointを経由してリクエストを送ることが一般化
   - GraphQLはRESTとは違った方法でAPI提供者とデータのやりとりを行うことを可能とする
 - ユーザーは各社のAPIを利用する事で、各サービスのデータを検索したりサイトで利用したり出来るようになります

##### REST(REpresentational State Transferの略称)(GraphQLに似たもの？)について
 - REST(REpresentational State Transfer)はWebサービスの設計モデル
 - Web APIの仕様を決める上でのアーキテクチャスタイル、つまり基本的な考え方
 - アーキテクチャスタイルというのは、日本語では「建築様式」と訳せますが、見方を変えるとそれはアーキテクチャに対する制約を意味する
 - RESTなWebサービスは、そのサービスのURIにHTTPメソッドでアクセスすることでデータの送受信を行う
 - RESTではこのようにデータとして扱いやすいJSON形式が一般的に利用されている
 - APIとして提供しているリソースを取得(GET)、リソースの登録(POST)、更新(PUT/PATCH)、削除(DELETE)などがRESTにより実現できる

 - RESTの設計原則
   - アドレス指定可能なURIで公開されていること
   - インターフェース(HTTPメソッドの利用)の統一がされていること
   - ステートレスであること
   - 処理結果がHTTPステータスコードで通知されること

 - RESTの考え方では、リソースはそれぞれ固有のURIを持つ
   - そしてそのURIにアクセスすることで、それぞれのリソースを操作することになる。
   - その際の操作はHTTPのメソッドを「正しく」使うことで行う
   - つまりHTTPの4つメソッド、すなわち「GET」「POST」「PUT」「DELETE」で何を行うかを伝える
   - 「リソース」とは、ブログの記事であったり、アップロードした写真であったり、もしくはWebページ全体のコンテンツであったりといった、ひとかたまりの情報を指す

 - CRUD操作：「生成（Create）」「読み取り（Read）」「更新（Update）」「削除（Delete）」のイニシャルを並べた用語のこと
 - これらの原則に則ったWebサービスをRESTfulなサービスというらしい
 - RESTは「リソース」を扱うための考え方

 - 過去のwebapiをまとめた上でデザインに起こす
 - おそらく数え切れないくらい....?
 - なぜRESTが使われるようになったか：Webアプリケーションの主流だったSOAPとWS-*の技術スタックの複雑になったから

##### How to use pmbok
 - yup

##### How to api into chatwork
 - api
 '''python
 import requests
 
api_token = '***'
base_url = 'https://api.chatwork.com/v2'
 
room_id = '66869579'
message = 'wassap wake up right now!!!'
 
post_message_url = '{}/rooms/{}/messages'.format(base_url, room_id)
headers = { 'X-ChatWorkToken': api_token }
params = { 'body': message }
 
response = requests.post(post_message_url, headers=headers, params=params)
print(response)
'''