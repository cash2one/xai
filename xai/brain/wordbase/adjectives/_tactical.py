

#calss header
class _TACTICAL():
	def __init__(self,): 
		self.name = "TACTICAL"
		self.definitions = [u'relating to tactics or done in order to achieve something: ', u'Tactical weapons are for use over short distances and, especially in the case of nuclear weapons, have a local effect only.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
