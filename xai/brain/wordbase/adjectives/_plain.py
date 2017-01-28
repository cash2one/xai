

#calss header
class _PLAIN():
	def __init__(self,): 
		self.name = "PLAIN"
		self.definitions = [u'not decorated in any way; with nothing added: ', u'paper that has no lines on it: ', u'obvious and clear to understand: ', u'(used for emphasis) complete: ', u'(especially of a woman or girl) not beautiful: ', u'a woman or girl who is not attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
