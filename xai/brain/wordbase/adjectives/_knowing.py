

#calss header
class _KNOWING():
	def __init__(self,): 
		self.name = "KNOWING"
		self.definitions = [u'showing that you know about something, even when it has not been talked about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
