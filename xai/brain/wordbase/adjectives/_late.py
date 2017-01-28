

#calss header
class _LATE():
	def __init__(self,): 
		self.name = "LATE"
		self.definitions = [u'used to refer to someone who has died: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
