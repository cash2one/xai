

#calss header
class _PROGNOSTIC():
	def __init__(self,): 
		self.name = "PROGNOSTIC"
		self.definitions = [u"relating to a doctor's judgment of the likely or expected development of a disease or of the chances of getting better"]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
