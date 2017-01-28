

#calss header
class _FEUDAL():
	def __init__(self,): 
		self.name = "FEUDAL"
		self.definitions = [u'relating to the social system of western Europe in the Middle Ages or any society that is organized according to rank. In a feudal society, people at one level of society receive land to live and work on from those higher than them in rank, and in return have to work for them and fight for them if necessary, sometimes also giving them some of the food they produce: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
