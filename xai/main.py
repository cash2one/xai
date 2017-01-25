
from xai.life.life import Life
from xai.brain.brain import Brain
from xai.body.body import Body
import time

# 
class AI():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        #
        self.brain = Brain()
        self.body = Body()
        self.life = Life()
        self.birthday = time.time()
        self.memory = self.brain.memory

        #
        # self.memory.word.build_word()


    def start(self):
    	print("------------------------------------------------------")
        print(r"""
                 ==                     ======
               ||  ||                     ||
              ||    ||                    ||
             ||       ||                  ||
            || ======= ||                 ||
           ||           ||                ||
          ||             ||               ||          
         ||               ||              ||         
        ||                 ||           ======                                                                                                                      
            Created and developed by Xing Wang
                     Bringing Computers to Science
     """)
    	print("------------------------------------------------------")
    	print("AI {0} started at {1}. \n\n".format(self.name, time.strftime("%Y-%m-%d %H:%M")))
    #
    def time(self):
        pass
    #
    def location(self):
        pass

# Run main function by default
if __name__ == "__main__":
    XAI = AI('Xing', 'male')
    XAI.start()
    XAI.life.training.word(filename = 'examples/word/cambtionary.dat')

