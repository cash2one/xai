

#calss header
class _FAST():
	def __init__(self,): 
		self.name = "FAST"
		self.definitions = [u'moving or happening quickly, or able to move or happen quickly: ', u'If your watch or clock is fast, it shows a time that is later than the correct time.', u'used to refer to photographic film that allows you to take pictures when there is not much light or when things are moving quickly', u'used to describe something that is full of speed and excitement: ', u'without moral principles: ', u'If the colour of a piece of clothing is fast, the colour does not come out of the cloth when it is washed.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
