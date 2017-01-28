

#calss header
class _BLIND():
	def __init__(self,): 
		self.name = "BLIND"
		self.definitions = [u'If something or someone is tested blind, either the people being tested or the person testing them, or both, do not know what is being tested.', u'to be flying an aircraft somewhere without being able to see where you are going: ', u'to be doing something without having any experience of doing it before or without having important information about what you are doing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
