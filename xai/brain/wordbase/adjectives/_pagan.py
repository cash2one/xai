

#calss header
class _PAGAN():
	def __init__(self,): 
		self.name = "PAGAN"
		self.definitions = [u'belonging or relating to a religion that worships many gods, especially one that existed before the main world religions: ', u'relating to religious beliefs that do not belong to any of the main religions of the world: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
