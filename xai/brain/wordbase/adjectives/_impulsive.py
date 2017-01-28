

#calss header
class _IMPULSIVE():
	def __init__(self,): 
		self.name = "IMPULSIVE"
		self.definitions = [u'showing behaviour in which you do things suddenly without any planning and without considering the effects they may have: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
