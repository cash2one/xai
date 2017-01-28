

#calss header
class _POINTED():
	def __init__(self,): 
		self.name = "POINTED"
		self.definitions = [u'A pointed object has a thin, sharp end or becomes much narrower at one end: ', u'A pointed remark, question, or manner is intended as a criticism of the person it is directed to: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
