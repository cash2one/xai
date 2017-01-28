

#calss header
class _FUNCTIONAL():
	def __init__(self,): 
		self.name = "FUNCTIONAL"
		self.definitions = [u'designed to be practical and useful rather than attractive: ', u'(of a machine, system, etc.) working in the usual way: ', u'performing a particular operation: ', u'relating to language functions, for example saying sorry, asking for something, or refusing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
