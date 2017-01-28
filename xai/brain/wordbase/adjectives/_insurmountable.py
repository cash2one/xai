

#calss header
class _INSURMOUNTABLE():
	def __init__(self,): 
		self.name = "INSURMOUNTABLE"
		self.definitions = [u'(especially of a problem or a difficulty) so great that it cannot be dealt with successfully: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
