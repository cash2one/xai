

#calss header
class _PULMONARY():
	def __init__(self,): 
		self.name = "PULMONARY"
		self.definitions = [u'relating to the lungs (= organs used for breathing): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
