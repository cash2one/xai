

#calss header
class _PRECIPITOUS():
	def __init__(self,): 
		self.name = "PRECIPITOUS"
		self.definitions = [u'If a slope is precipitous, it is very steep: ', u'If a reduction or increase is precipitous, it is fast or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
