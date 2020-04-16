<template>
<!-- 绑定事件 -->
    <div class="slider-component" @mouseover="clearInv" @mouseout="runInv">
        <div v-show='index===nowIndex' v-for="(imgUrl,index) in sliderImgList" :key="index" class="slider-item item1"  v-bind:class="['item'+index]">
            <a href="">
                <img v-bind:src=imgUrl alt="">
            </a>
        </div>

        <ul class="slider-dots">
            <li>&lt;</li>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>&gt;</li>
        </ul>
    </div>
</template>

<script>
export default{
    data() {
        return {
            nowIndex:0,
            sliderImgList:[require('../assets/pic1.png'),require('../assets/pic2.png'),require('../assets/pic3.png'),require('../assets/pic4.png')]
        }
    },
    // 钩子函数、
    methods: {
        autoPlay(){
            this.nowIndex++;
            if(this.nowIndex===4){
                this.nowIndex=0
            }
        },
        // 定时切换
        runInv(){
            this.invId=setInterval(this.autoPlay,1000)
            
        },
        clearInv(){
            clearInterval(this.invId)
           
        },
        

    },
    created() {
        console.log("haominmin")
        // 调用函数
        this.runInv()
    },
}

</script>

<style >
.slider-component{
    width: 900px;
    height: 500px;
    /* 溢出影藏 */
    overflow: hidden;
    position: relative;
}

.slider-item{
    width: 900px;
    height: 500px;
    position: absolute;

}
.item1{
    /* 值越大就这上面 */
    z-index: 100;
}

.item2{
    z-index: 90;
}

.item3{
    z-index: 80;
}

.item4{
    z-index: 70;
}

.slider-dots{
    position: absolute;
    right: 50px;
    bottom: 20px;
    z-index: 200;
    
}
.slider-dots li{
    width: 20px;
    height: 20px;
    background: black;
    /* 横着 */
    border-radius: 50%;
    float: left;
    color: white;
    text-align: center;
    opacity: 0.6;
    margin: 0 auto;
    
}

</style>

