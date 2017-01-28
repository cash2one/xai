

#calss header
class _ANTIDEPRESSANT():
	def __init__(self,): 
		self.name = "ANTIDEPRESSANT"
		self.definitions = [u'An anti-depressant drug is one that is used to reduce feelings of sadness and worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
