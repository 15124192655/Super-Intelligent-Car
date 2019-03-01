let gpio=require('rpi-gpio');
let ini=require('ini');
let fs=require('fs');

let gpiop=gpio.promise;




class CarController{
    constructor(){
        let config=ini.parse(fs.readFileSync('./config.ini','utf-8'));
        this.L1=config.car.LEFT_FRONT_1;
        this.L2=config.car.LEFT_FRONT_2;
        this.R1=config.car.RIGHT_FRONT_1;
        this.R2=config.car.RIGHT_FRONT_2;

        this.initPin();
    }
    async initPin(){
        await gpiop.setup(config.car.LEFT_FRONT_1,'out');
        await gpiop.setup(config.car.LEFT_FRONT_2,'out');
        await gpiop.setup(config.car.RIGHT_FRONT_1,'out');
        await gpiop.setup(config.car.RIGHT_FRONT_2,'out');
    }
    async reset(){
        await gpiop.write(this.L1,false);
        await gpiop.write(this.L2,false);
        await gpiop.write(this.R1,false);
        await gpiop.write(this.R2,false);
    }

}
car=new CarController();