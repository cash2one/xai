

#calss header
class _DOWN():
	def __init__(self,): 
		self.name = "DOWN"
		self.definitions = [u'unhappy; unable to feel excited or energetic about anything: ', u'(of a system or machine, especially a computer) not in operation or not working, usually only for a limited period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
