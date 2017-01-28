

#calss header
class _GREGARIOUS():
	def __init__(self,): 
		self.name = "GREGARIOUS"
		self.definitions = [u'(of people) liking to be with other people : ', u'(especially of animals) living in groups']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
