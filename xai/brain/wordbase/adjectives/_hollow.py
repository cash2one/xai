

#calss header
class _HOLLOW():
	def __init__(self,): 
		self.name = "HOLLOW"
		self.definitions = [u'having a hole or empty space inside: ', u'If you have hollow cheeks or eyes, your cheeks curve in or your eyes look deep in your head because you are old, tired, or ill.', u'(of situations, feelings, or words) without value, or not true or sincere: ', u'(of sound) as if made by hitting an empty container: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
