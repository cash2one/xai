

#calss header
class _COHERENT():
	def __init__(self,): 
		self.name = "COHERENT"
		self.definitions = [u'If an argument, set of ideas, or a plan is coherent, it is clear and carefully considered, and each part of it connects or follows in a natural or reasonable way.', u'If someone is coherent, you can understand what that person says: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
