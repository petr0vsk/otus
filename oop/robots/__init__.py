# 1
from  .fatherbot  import FatherBot      # архетип-метакласс
from  .bot        import Bot            # робот
from  .candrive   import CanDrive       # класс-миксин обеспечивающий возможность ехать по поверхности
from  .canfloat   import CanFloat       # класс-миксин обеспечивающий возможность летать 
from  .canfly     import CanFly         # класс-миксин обеспечивающий возможность плыть 
from  .roverbot   import RoverBot       # самодвижущийся робот-автомобиль
from  .flyingboat import FlyingBoatBot  # летающая лодка-робот
from  .engine     import Engine, base_engine, aviation_engine, marine_engine, hi_power_engine # датакласс для движков

