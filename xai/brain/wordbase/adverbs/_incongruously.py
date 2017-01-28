

#calss header
class _INCONGRUOUSLY():
	def __init__(self,): 
		self.name = "INCONGRUOUSLY"
		self.definitions = [u'in a way that seems strange because it is different from other things around it or from what is generally happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
