

#calss header
class _INTROSPECTIVE():
	def __init__(self,): 
		self.name = "INTROSPECTIVE"
		self.definitions = [u'examining and considering your own ideas, thoughts, and feelings, instead of talking to other people about them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
