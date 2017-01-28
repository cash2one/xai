

#calss header
class _SCENTED():
	def __init__(self,): 
		self.name = "SCENTED"
		self.definitions = [u'having a pleasant strong smell, usually because a pleasant-smelling substance has been added to it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
