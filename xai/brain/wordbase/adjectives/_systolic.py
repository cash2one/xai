

#calss header
class _SYSTOLIC():
	def __init__(self,): 
		self.name = "SYSTOLIC"
		self.definitions = [u'used to describe the phase of the blood pressure cycle when the ventricles of the heart have their strongest contractions against the blood vessel walls: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
