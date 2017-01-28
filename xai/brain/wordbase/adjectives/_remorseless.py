

#calss header
class _REMORSELESS():
	def __init__(self,): 
		self.name = "REMORSELESS"
		self.definitions = [u'severe and showing no sadness or guilt: ', u'never stopping or impossible to stop: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
