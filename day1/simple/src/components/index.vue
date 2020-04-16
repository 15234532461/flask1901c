<template>
    <div class="index-wrapper" >
        <div class="index-left" >
            <div class="index-left-block all-products">
                <h2>全部产品</h2>
                <template v-for="product in productList" >
                    <h3>{{ product.title }}</h3>
                <ul>
                    <li v-for="item in product.list">
                        <a v-bind:href="item.url">{{ item.title }}</a>
                        <span class="hot-tag" v-if="item.hot" >HOT</span>
                    </li>
                </ul>
                <hr v-if="!product.list" />
                </template>
            </div>
            <template>
                <div class="index-left-block lastest-news">
                <h2>最新消息</h2>
                <ul>
                    <li v-for="xiaoxis in newsList">
                        <a v-bind:href="xiaoxis.url">{{ xiaoxis.title }}</a>
                    </li>
                </ul>
                </div>
            </template>
            
        </div>
        <div class="index-right" >
            <div style="font-size:40px;text-align:center;line-height:300px;width:900px;background: #4fc08d;" >
                slider
            </div>
            <div class="index-board-list">
                <div class="index-board-item" >
                    <div class="index-board-item-inner">
                    <h2>联想电脑</h2>
                    <p>联想电脑就是牛</p>
                    <div class="index-board-button" >立即购买</div>
                    </div>
                </div>
                <div class="index-board-item" >
                    <div class="index-board-item-inner">
                    <h2>联想电脑</h2>
                    <p>联想电脑就是牛</p>
                    <div class="index-board-button" >立即购买</div>
                    </div>
                </div>
                <div class="index-board-item" >
                    <div class="index-board-item-inner">
                    <h2>联想电脑</h2>
                    <p>联想电脑就是牛</p>
                    <div class="index-board-button" >立即购买</div>
                    </div>
                </div>
                <div class="index-board-item" >
                    <div class="index-board-item-inner">
                    <h2>联想电脑</h2>
                    <p>联想电脑就是牛</p>
                    <div class="index-board-button" >立即购买</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>>

<script>
import axios from "axios";
export default {
    mounted() {
        var that=this
        axios.get("/getNewsList")
          .then((response) => {
              //headle success
              console.log(response);
              that.newsList = response.data.list
          })
          .catch((error) => {
              // handle error
              console.log(error);
          });
    },
    data() {
        return {
            newsList:[
                
            ],
            // xiaoxi:{
            //         name:[
            //             {
            //                 content: "手机不是终点，汽车才是华为的下一个目标",
            //                 url: "https://tech.sina.com.cn/mobile/n/n/2020-04-13/doc-iircuyvh7041870.shtml"
            //             },
            //             {
            //                 content: "屡次突破拍照极限，华为P40带来手机摄影更多想象",
            //                 url: "https://baijiahao.baidu.com/s?id=1663850916373477627&wfr=spider&for=pc"
            //             },
            //             {
            //                 content: "联想刘军：新财年国内PC份额涨2% 服务营收破70亿元",
            //                 url: "http://finance.sina.com.cn/stock/relnews/hk/2020-04-15/doc-iircuyvh7903952.shtml"
            //             },
            //             {
            //                 content: "最新消息：苹果将今晚发布iPhone9(SE2)!",
            //                 url: "http://news.ifeng.com/c/7vgvg1USoTg"
            //             },
            //             {
            //                 content: "售价惊人的外星人Aurora台式电脑将来，你会买吗？",
            //                 url: "https://baijiahao.baidu.com/s?id=1612316559468102586&wfr=spider&for=pc"
            //             },
            //         ]
            //     },
            productList:{
                pc: {
                    title:"PC产品",
                    list:[
                        {
                            title:"数据统计",
                            url:"http://starcraft.com"
                        },
                        {
                            title: "数据预测",
                            url: "http://warcraft.com",
                            hot:true,
                        },
                        {
                            title: "流量分析",
                            url: "http://overwatch.com",
                            hot: true
                        },
                        {
                            title: "广告发布",
                            url: "http://hearstone.com"
                        }
                    ]
                },
                app: {
                    title:"手机应用类",
                    last:true,
                    list:[
                        {
                          title: "91助手",
                          url: "http://weixin.com"
                        },
                        {
                          title: "产品助手",
                          url: "http://weixin.com",
                          hot:true,
                        },
                        {
                          title: "智能地图",
                          url: "http://maps.com",
                        },
                        {
                          title: "语音助手",
                          url: "http://phone.com",
                          hot:true,
                        }
                    ]
                }
            }
        }
    },
}
</script>
<style>
   .index-wrapper{
       width: 1200px;
       margin:0 auto;
       display: flex;
   }
    .index-left{
        width: 300px;

    }
    .index-right{
        width: 900px;
    }
    .index-left-block{
        margin: 15px;
        background: white;
        box-shadow: 0 0 1px #ddd;
        border-radius: 0 0 10px 10px;
    }
    .index-left-block h2{
        color: #fff;
        background: #4fc08d;
        padding: 10px 15px;
        margin-bottom: 15px;
    }
    .all-products h3{
        padding: 0 15px 5px 15px;
        font-weight: bolder;
        color: #222;
    }
    .index-left-block ul{
        padding: 0 15px 5px 15px;
    }
    .hot-tag{
        color: white;
        background: purple;
        font-size: 12px;
    }
    .index-board-list{
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }
    .index-board-item{
        width: 400px;
        background: #fff;
        box-shadow: 0 0 1px #ddd;
        margin-bottom: 20px;
    }
    .index-board-item-inner{
        height: 125px;
        padding-left: 120px;
        background-image: url(../assets/logo.png);
        background-repeat: no-repeat;
        background-size: 20%;
        background-position: 20px;
    }
    .index-board-item-inner h2{
        font-size: 18px;
        font-weight: bolder;
        color: #222;
        margin-bottom: 15px;
    }
    .index-board-item-inner p{
        margin-bottom: 15px;
    }
    .index-board-button{
        width: 80px;
        height: 30px;
        line-height: 30px;
        color: #fff;
        background: greenyellow;
        border-radius: 5px;
        text-align: center;
    }
    

</style>