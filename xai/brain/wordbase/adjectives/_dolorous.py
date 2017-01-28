

#calss header
class _DOLOROUS():
	def __init__(self,): 
		self.name = "DOLOROUS"
		self.definitions = [u'sad, or causing sadness or emotional suffering']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
