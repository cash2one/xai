

#calss header
class _CRACKERS():
	def __init__(self,): 
		self.name = "CRACKERS"
		self.definitions = [u'silly, stupid, or slightly mentally ill']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
