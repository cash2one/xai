

#calss header
class _EVASIVE():
	def __init__(self,): 
		self.name = "EVASIVE"
		self.definitions = [u'answering questions in a way that is not direct or clear, especially because you do not want to give an honest answer: ', u'done to avoid something bad happening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
