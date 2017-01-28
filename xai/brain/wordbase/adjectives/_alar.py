

#calss header
class _ALAR():
	def __init__(self,): 
		self.name = "ALAR"
		self.definitions = [u'relating to a body part that is shaped like a wing', u'relating to the axilla (= the armpit)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
