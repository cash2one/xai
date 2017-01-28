

#calss header
class _PETTIFOGGING():
	def __init__(self,): 
		self.name = "PETTIFOGGING"
		self.definitions = [u'Pettifogging people give too much attention to small unimportant details in a way that shows a limited mind: ', u'Pettifogging rules or details are too small and not important enough to give attention to.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
