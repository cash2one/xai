

#calss header
class _EXECUTABLE():
	def __init__(self,): 
		self.name = "EXECUTABLE"
		self.definitions = [u'An executable file or program can be understood by the operating system of a computer and makes the computer perform a particular task.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
