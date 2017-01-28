

#calss header
class _DAIRY():
	def __init__(self,): 
		self.name = "DAIRY"
		self.definitions = [u'used to refer to cows that are used for producing milk, rather than meat, or to foods that are made from milk, such as cream, butter, and cheese: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
