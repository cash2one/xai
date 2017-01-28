

#calss header
class _SICK():
	def __init__(self,): 
		self.name = "SICK"
		self.definitions = [u'physically or mentally ill; not well or healthy: ', u'feeling ill as if you are going to vomit: ', u'to vomit: ', u'feeling strong unpleasant emotions, especially anger or disgust: ', u'cruel or offensive: ', u'very good, excellent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
