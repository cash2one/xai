

#calss header
class _CONFIRMED():
	def __init__(self,): 
		self.name = "CONFIRMED"
		self.definitions = [u'used to say that someone who has had a particular habit or way of life for a long time and is unlikely to change: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
