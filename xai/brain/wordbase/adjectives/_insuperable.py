

#calss header
class _INSUPERABLE():
	def __init__(self,): 
		self.name = "INSUPERABLE"
		self.definitions = [u'(especially of a problem) so great or severe that it cannot be defeated or dealt with successfully']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
