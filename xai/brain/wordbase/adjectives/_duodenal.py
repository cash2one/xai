

#calss header
class _DUODENAL():
	def __init__(self,): 
		self.name = "DUODENAL"
		self.definitions = [u'of the duodenum (= the part of the small bowel the stomach empties into): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
