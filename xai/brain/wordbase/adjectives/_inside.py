

#calss header
class _INSIDE():
	def __init__(self,): 
		self.name = "INSIDE"
		self.definitions = [u'(of information) obtained by someone in a group, organization, or company and therefore involving special or secret knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
