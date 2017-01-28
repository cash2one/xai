

#calss header
class _MOVED():
	def __init__(self,): 
		self.name = "MOVED"
		self.definitions = [u'having strong feelings of sadness or sympathy, because of something someone has said or done: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
