

#calss header
class _OMNIPRESENT():
	def __init__(self,): 
		self.name = "OMNIPRESENT"
		self.definitions = [u'present or having an effect everywhere at the same time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
