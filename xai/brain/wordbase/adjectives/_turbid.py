

#calss header
class _TURBID():
	def __init__(self,): 
		self.name = "TURBID"
		self.definitions = [u'(of a liquid) not transparent because a lot of small pieces of matter are held in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
