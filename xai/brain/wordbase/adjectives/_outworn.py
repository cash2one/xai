

#calss header
class _OUTWORN():
	def __init__(self,): 
		self.name = "OUTWORN"
		self.definitions = [u'(especially of an idea or phrase) old-fashioned and used too often in the past, so no longer useful or important']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
